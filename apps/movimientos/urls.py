from django.urls import path
from .views.ingresos.views import ListadoIngresos, DetalleIngresoView, RegistrarIngreso, BuscarProductosView, BuscarProductosIngresoView
from .views.solicitudes_online.views import MisSolicitudesMedOnline, DetalleMiSolicitudOnline, RegistrarMiSolicitud, RegistrarBeneficiado
from .views.solicitudes.views import (
    SolicitudesMed, 
    EditarSolicitud, 
    MedicamentoEntregado, 
    DetalleSolicitudMed, 
    RegistrarSolicitudPresencial, 
    RegistrarBeneficiadoFisico, 
    RegistrarPerfilFisico, 
    MedicamentoEnEsperaEntrega,
    VerificarDatosSolicitudMed,
    RechazarSolicitudMedicamento
)
from .views.mantenimiento.views import ListadoTipoMovi, ActualizarTipoMovi, RegistrarTipoMovi
from .views.jornadas.views import (
    MisSolicitudesJornadas, 
    DetalleMiJornada, 
    RegistrarMiJornada,
    BuscarBeneficiadoComunidadView,
    BuscarBeneficiadoComunidadModificacionView,
    SolicitudesJornadas,
    DetalleJornadaView,
    EditarJornada,
    JornadaCompletada,
    RechazarSolicitudJornada,
    ActualizarJornada
)

from .reportes import (
    TodasLasJornadas,
    TodasLasSolicitudes
)

urlpatterns = [
    # INGRESOS
    path('listado-de-ingresos/', ListadoIngresos.as_view(), name='listado_ingresos'),
    path('detalle-de-ingreso/<int:pk>/', DetalleIngresoView.as_view(), name='detalle_ingreso'),
    path('registrar-ingreso/', RegistrarIngreso.as_view(), name='registrar_ingreso'),
    path('buscar-productos/', BuscarProductosView.as_view(), name='buscar_productos'),
    path('buscar-productos-ingresos/', BuscarProductosIngresoView.as_view(), name='buscar_productos_ingresos'),
    # MIS SOLICITUDES
    path('mis-solictudes-de-medicamentos/', MisSolicitudesMedOnline.as_view(), name='mis_solicitudes_medicamentos'),
    path('mi-solictud-de-medicamento/<int:pk>/', DetalleMiSolicitudOnline.as_view(), name='mi_solicitud_medicamento'),
    path('registrar-mi-solicitud/', RegistrarMiSolicitud.as_view(), name='registrar_mi_solicitud'),
    path('registrar-beneficiado-modal/', RegistrarBeneficiado.as_view(), name='registrar_beneficiado_modal'),

    # SOLICITUDES
    path('solictudes-de-medicamentos/', SolicitudesMed.as_view(), name='listado_solicitudes_medicamentos'),
    path('registrar-solicitud/', RegistrarSolicitudPresencial.as_view(), name='registrar_solicitud_presencial'),
    path('detalle-de-solicitud-de-medicamento/<int:pk>/', DetalleSolicitudMed.as_view(), name='detalle_solicitud_med'),
    path('modificar-solicitud-de-medicamentos/<int:pk>/', EditarSolicitud.as_view(), name='modificar_solicitudes_medicamentos'),
    path('solicitud-de-medicamento-entregado/<int:pk>/', MedicamentoEntregado.as_view(), name='solicitud_de_medicamento_entregado'),
    path('solicitud-de-medicamento-en-espera-de-entrega/<int:pk>/', MedicamentoEnEsperaEntrega.as_view(), name='solicitud_de_medicamento_en_espera_entrega'),
    path('solicitud-de-medicamento-verificada/<int:pk>/', VerificarDatosSolicitudMed.as_view(), name='solicitud_de_medicamento_verificada'),
    path('rechazar-solicitud-de-medicamento/', RechazarSolicitudMedicamento.as_view(), name='rechazar_solicitud_medicamento'),
    path('registrar-beneficiado-fisico-modal/', RegistrarBeneficiadoFisico.as_view(), name='registrar_beneficiado_fisico_modal'),
    path('registrar-perfil-fisico-modal/', RegistrarPerfilFisico.as_view(), name='registrar_perfil_fisico_modal'),

    # TIPO MOVIMIENTOS
    path('listado-de-tipos-movimientos/', ListadoTipoMovi.as_view(), name='listado_tipo_movi'),
    path('agregar-tipos-movimientos/', RegistrarTipoMovi.as_view(), name='nuevo_tipo_movi'),
    path('editar-tipos-movimientos/', ActualizarTipoMovi.as_view(), name='edit_tipo_movi'),

    # JORNADAS
    path('mis-solicitudes-de-jornadas/', MisSolicitudesJornadas.as_view(), name='mi_listado_jornadas'),
    path('detalle-de-mi-solicitud-de-jornada/<int:pk>/', DetalleMiJornada.as_view(), name='detalle_mi_jornada'),
    path('registrar-mi-jornada/', RegistrarMiJornada.as_view(), name='registrar_mi_jornada'),
    path('cargar-comunidad/', BuscarBeneficiadoComunidadView.as_view(), name='cargar_comunidad'),
    path('cargar-comunidad-modificacion/', BuscarBeneficiadoComunidadModificacionView.as_view(), name='cargar_comunidad_modificacion'),
    path('solicitudes-de-jornadas/', SolicitudesJornadas.as_view(), name='listado_jornadas'),
    path('detalle-de-solicitud-de-jornada/<int:pk>/', DetalleJornadaView.as_view(), name='detalle_jornada'),
    path('modificar-jornada/<int:pk>/', EditarJornada.as_view(), name='modificar_jornada'),
    path('jornada-completada/<int:pk>/', JornadaCompletada.as_view(), name='jornada_completada'),
    path('rechazar-jornada-de-medicamento/', RechazarSolicitudJornada.as_view(), name='rechazar_jornada_medicamento'),
    path('actualizar-jornada-de-medicamento/', ActualizarJornada.as_view(), name='actualizar_jornada_medicamento'),

    # reportes
    path('reporte/listado-de-jornada-zona/<int:pk>/', TodasLasJornadas.as_view(), name='l_jornada'),
    path('reporte/listado-de-solicitudes/', TodasLasSolicitudes.as_view(), name='t_solicitudes'),

]
