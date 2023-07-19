"""Djaizz Model Views."""


from inspect import isclass
from typing import Literal, Union

from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from django_plotly_dash.dash_wrapper import DjangoDash
from django_plotly_dash.models import DashApp, StatelessApp

from gradio.inputs import Dropdown
from gradio.interface import Interface

from djaizz.model.models import AIModel


def model_ui(request: HttpRequest,
             model_class_or_instance_name_or_uuid: str,
             ui_type: Literal['dash', 'gradio']) \
        -> Union[Http404, HttpResponse, HttpResponseRedirect]:
    # pylint: disable=unused-argument
    """Launch AI Model class/instance's Dash or Gradio UI."""
    if model_class_or_instance_name_or_uuid in \
            (model_subclasses_by_name := AIModel.subclasses_by_name):
        # pylint: disable=trailing-whitespace,unsubscriptable-object
        if not (model_names_or_uuids :=   # noqa: W291
                (model := model_subclasses_by_name[
                    model_class_or_instance_name_or_uuid]).names_or_uuids):
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

        model_names_or_uuids: list[str] = model.names_or_uuids

    if ui_type == 'dash':
        if not isinstance(dash_ui := model.dash_ui, DjangoDash):
            raise Http404(f'*** {model} DOES NOT HAVE A DASH UI ***')

        # if `model` is an AIModel instance, then render the view for its class
        if isinstance(model, AIModel):
            model_class_or_instance_name_or_uuid = type(model).__name__

        ((django_dash_stateless_app :=
          StatelessApp.objects.get_or_create(
            app_name=model_class_or_instance_name_or_uuid)[0])
         ._stateless_dash_app_instance) = dash_ui

        return render(
            request=request, template_name='Djaizz-Model-Dash-App.html',
            context={'django_dash_app':
                     DashApp.objects.get_or_create(
                        stateless_app=django_dash_stateless_app,
                        instance_name=model_class_or_instance_name_or_uuid)[0]
                     },
            content_type=None, status=None, using=None)

    if ui_type == 'gradio':
        if not isinstance(gradio_interface := model.gradio_ui, Interface):
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
                # (Callable, Union[tuple[str, str], list[tuple[str, str]]]) -
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
