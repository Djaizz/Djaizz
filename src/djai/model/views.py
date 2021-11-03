"""DjAI Model Views."""


from inspect import isclass
from typing import Literal, Union
from typing import Dict, List   # Py3.9+: use generic types

from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from polymorphic.base import PolymorphicModelBase

from django_plotly_dash.dash_wrapper import DjangoDash
from django_plotly_dash.models import DashApp, StatelessApp

from gradio.inputs import Dropdown
from gradio.interface import Interface

from djai.model.models import AIModel


def model_ui(request: HttpRequest,
             model_class_or_instance_name_or_uuid: str,
             ui_type: Literal['dash', 'gradio']) \
        -> Union[Http404, HttpResponse, HttpResponseRedirect]:
    # pylint: disable=unused-argument
    """Launch AI Model class/instance's Dash or Gradio UI."""
    model_subclasses_by_name: Dict[str, PolymorphicModelBase] = \
        AIModel.subclasses_by_name

    # pylint: disable=unsupported-membership-test
    if model_class_or_instance_name_or_uuid in model_subclasses_by_name:
        # pylint: disable=unsubscriptable-object
        model: PolymorphicModelBase = \
            model_subclasses_by_name[model_class_or_instance_name_or_uuid]

        model_names_or_uuids: List[str] = model.names_or_uuids

        if not model_names_or_uuids:
            raise Http404('*** MODEL CLASS ' +
                          model_class_or_instance_name_or_uuid +
                          ' HAS NO INSTANCES ***')

    else:
        try:
            model: AIModel = AIModel.get_by_name_or_uuid(
                name_or_uuid=model_class_or_instance_name_or_uuid)

        except AIModel.DoesNotExist as ai_model_does_not_exist:
            raise Http404('*** MODEL INSTANCE ' +
                          model_class_or_instance_name_or_uuid +
                          ' NOT FOUND ***') from ai_model_does_not_exist

        model_names_or_uuids: List[str] = model.names_or_uuids

    if ui_type == 'dash':
        dash_ui: DjangoDash = model.dash_ui

        if not isinstance(dash_ui, DjangoDash):
            raise Http404(f'*** {model} DOES NOT HAVE A DASH UI ***')

        django_dash_stateless_app: StatelessApp = \
            StatelessApp.objects.get_or_create(
                app_name=model_class_or_instance_name_or_uuid)[0]
        # insert `dash_ui` into `django_dash_stateless_app`'s internals
        django_dash_stateless_app._stateless_dash_app_instance = dash_ui

        django_dash_app: DashApp = \
            DashApp.objects.get_or_create(
                stateless_app=django_dash_stateless_app,
                instance_name=model_class_or_instance_name_or_uuid)[0]

        return render(request=request,
                      template_name='DjAI-Model-Dash-App.html',
                      context=dict(django_dash_app=django_dash_app),
                      content_type=None, status=None, using=None)

    if ui_type == 'gradio':
        gradio_interface: Interface = model.gradio_ui

        if not isinstance(gradio_interface, Interface):
            raise Http404(f'*** {model} DOES NOT HAVE A GRADIO UI ***')

        assert isinstance(gradio_interface.predict, list), \
            TypeError(f'*** {gradio_interface.predict} NOT A LIST ***')
        func: callable = gradio_interface.predict.pop()
        assert not gradio_interface.predict, \
            ValueError(f'*** {gradio_interface.predict} NOT AN EMPTY LIST ***')
        gradio_interface.predict.append(
            lambda model_name_or_uuid, *args:
            func(model.get_by_name_or_uuid(name_or_uuid=model_name_or_uuid),
                 *args))

        gradio_interface.input_components.insert(
            0,
            Dropdown(choices=model_names_or_uuids,
                     type='value',
                     default=(model_names_or_uuids[0]
                              if isclass(model)
                              else model.name_or_uuid),
                     label='AI Model Name or UUID'))

        _gradio_app, _gradio_path_to_local_server, gradio_share_url = \
            gradio_interface.launch(
                inline=False,
                # (bool) - whether to display in the interface inline
                # on python notebooks.

                inbrowser=True,
                # (bool) - whether to automatically launch the interface
                # in a new tab on the default browser.

                share=True,
                # (bool) - whether to create a publicly shareable link
                # from your computer for the interface.

                debug=False,
                # (bool) - if True, and the interface was launched
                # from Google Colab, prints the errors in the cell output.

                auth=None,
                # (Callable, Union[Tuple[str, str], List[Tuple[str, str]]]) -
                # If provided, username and password
                # (or list of username-password tuples)
                # required to access interface.
                # Can also provide function that takes username and password
                # and returns True if valid login.

                auth_message=None,
                # (str) - If provided, HTML message provided on login page.

                private_endpoint=None,
                prevent_thread_lock=False)

        return redirect(to=gradio_share_url, permanent=False)

    raise Http404('*** ui_type MUST BE EITHER "dash" or "gradio" ***')
