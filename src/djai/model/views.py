"""DjAI Model Views."""


from inspect import isclass
from typing import Union

from django.http.response import Http404, HttpResponseRedirect
from polymorphic.base import PolymorphicModelBase

from gradio.inputs import Dropdown
from gradio.interface import Interface

from djai.model.models import AIModel


def gradio_ui(request, model_class_or_instance_name_or_uuid: str) \
        -> Union[Http404, HttpResponseRedirect]:
    # pylint: disable=unused-argument
    """Launch AI Model class/instance's Gradio UI."""
    model_subclasses_by_name: dict[str, PolymorphicModelBase] = \
        AIModel.subclasses_by_name

    # pylint: disable=unsupported-membership-test
    if model_class_or_instance_name_or_uuid in model_subclasses_by_name:
        # pylint: disable=unsubscriptable-object
        model: PolymorphicModelBase = \
            model_subclasses_by_name[model_class_or_instance_name_or_uuid]

        model_names_or_uuids: list[str] = model.names_or_uuids

        if not model_names_or_uuids:
            return Http404('*** MODEL CLASS ' +
                           model_class_or_instance_name_or_uuid +
                           ' HAS NO INSTANCES ***')

    else:
        try:
            model: AIModel = AIModel.get_by_name_or_uuid(
                name_or_uuid=model_class_or_instance_name_or_uuid)

        except AIModel.DoesNotExist:
            return Http404('*** MODEL INSTANCE ' +
                           model_class_or_instance_name_or_uuid +
                           ' NOT FOUND ***')

        model_names_or_uuids: list[str] = model.names_or_uuids

    gradio_interface: Interface = model.gradio_ui

    if not isinstance(gradio_interface, Interface):
        return Http404(f'*** {model} DOES NOT HAVE A (CORRECT) GRADIO UI ***')

    assert isinstance(gradio_interface.predict, list), \
        TypeError(f'*** {gradio_interface.predict} NOT A LIST ***')
    func: callable = gradio_interface.predict.pop()
    assert not gradio_interface.predict, \
        ValueError(f'*** {gradio_interface.predict} NOT AN EMPTY LIST ***')
    gradio_interface.predict.append(
        lambda model_name_or_uuid, *args:
        func(model.get_by_name_or_uuid(name_or_uuid=model_name_or_uuid), *args)
    )

    gradio_interface.input_components.insert(
        0,
        Dropdown(choices=model_names_or_uuids,
                 type='value',
                 default=(model_names_or_uuids[0]
                          if isclass(model)
                          else model.name_or_uuid),
                 label='H1st Model Name or UUID'))

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

    return HttpResponseRedirect(redirect_to=gradio_share_url)
