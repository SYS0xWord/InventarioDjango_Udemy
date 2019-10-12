import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import FacturaCompra, Lote
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


@permission_required('cmp.can_mark_returned')
def reporte_compras(request):
    template_path = 'cmp/compras_print_all.html'
    today = timezone.now()
    compras = FacturaCompra.objects.all()
    context = {
        'obj': compras,
        'today': today,
        'request': request
    }
    response = HttpResponse(content_type='application/pdf')
    response['Conten-Diposition'] = 'inline; filename="todas_compras.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
        return HttpResponse('Tenemos algun problema <pre>' + html + '</pre>')
    return response
