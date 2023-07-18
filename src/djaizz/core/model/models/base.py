"""Djaizz base AIModel class."""


from abc import abstractmethod
from json.decoder import JSONDecoder
from sys import version_info
from typing import Any, Optional

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields import CharField
from django.db.models.fields.json import JSONField
from django.utils.functional import classproperty

from polymorphic.base import PolymorphicModelBase
from polymorphic.models import PolymorphicModel

from django_plotly_dash import DjangoDash

# pylint: disable=ungrouped-imports
try:
    from dash import dcc, html
except ImportError:
    import dash_core_components as dcc
    import dash_html_components as html
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from gradio.interface import Interface
from gradio.outputs import JSON as JSONOutput   # noqa: N811

from djutil.models import _ModelWithUUIDPKAndOptionalUniqueNameAndTimestampsABC

from djaizz.model.apps import DjaizzModelModuleConfig
from djaizz.util import PGSQL_IDENTIFIER_MAX_LEN, full_qual_name

if version_info >= (3, 9):
    from collections.abc import Generator, Sequence
else:
    from typing import Generator, Sequence  # pylint: disable=ungrouped-imports


__all__: Sequence[str] = 'AIModel', '_AIModelWithArtifactFilesABC'


class AIModel(PolymorphicModel,
              _ModelWithUUIDPKAndOptionalUniqueNameAndTimestampsABC):
    """Djaizz base AIModel class."""

    params: JSONField = \
        JSONField(
            verbose_name='Model Parameters',
            help_text='Model Parameters',

            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,

            null=True,
            blank=True,
            choices=None,
            db_column=None,
            db_index=False,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages={},
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta(_ModelWithUUIDPKAndOptionalUniqueNameAndTimestampsABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        verbose_name: str = 'AI Model'
        verbose_name_plural: str = 'AI Models'

        db_table: str = (f'{DjaizzModelModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name: str = 'ai_models'

    @abstractmethod
    def fit(self, **kwargs) -> Any:
        """Fit."""
        raise NotImplementedError

    @abstractmethod
    def predict(self, **kwargs) -> Any:
        """Predict."""
        raise NotImplementedError

    @classproperty
    def _subclasses(cls) -> Generator[PolymorphicModelBase, None, None]:   # noqa: E501,N805
        # pylint: disable=no-self-argument
        """Generate AIModel class's subclasses."""
        for subclass in cls.__subclasses__():
            yield subclass
            yield from subclass._subclasses

    @classproperty
    def subclasses(cls) -> list[PolymorphicModelBase]:   # noqa: N805
        # pylint: disable=no-self-argument
        """List of AIModel class's subclasses."""
        return list(cls._subclasses)

    @classproperty
    def subclass_names(cls) -> list[str]:   # noqa: N805
        # pylint: disable=no-self-argument
        """List of AIModel class's subclasses' names."""
        return [s.__name__
                for s in cls._subclasses   # pylint: disable=not-an-iterable
                ]

    @classproperty
    def subclasses_by_name(cls) -> dict[str, PolymorphicModelBase]:   # noqa: E501,N805
        # pylint: disable=no-self-argument
        """Return AIModel class's subclass-by-name dictionary.

        Dictionary mapping from AIModel class's subclasses' names
        to such subclasses.
        """
        return {s.__name__: s
                for s in cls._subclasses   # pylint: disable=not-an-iterable
                }

    @classproperty
    def subclass_full_qual_names(cls) -> list[str]:   # noqa: N805
        # pylint: disable=no-self-argument
        """List of AIModel class's subclasses' fully-qualified names."""
        return [full_qual_name(s)
                for s in cls._subclasses   # pylint: disable=not-an-iterable
                ]

    @classproperty
    def subclasses_by_full_qual_name(cls) -> dict[str, PolymorphicModelBase]:   # noqa: E501,N805
        # pylint: disable=no-self-argument
        """Return AIModel class's subclass-by-fully-qualified name dict.

        Dictionary mapping from AIModel class's subclasses'
        fully-qualified names to such subclasses.
        """
        return {full_qual_name(s): s
                for s in cls._subclasses   # pylint: disable=not-an-iterable
                }

    @classproperty
    def dash_ui(cls) -> DjangoDash:   # noqa: N805
        # pylint: disable=no-self-argument
        """Return the AIModel class's Dash Interface."""
        app = DjangoDash(name=cls.__name__,
                         serve_locally=False,
                         add_bootstrap_links=True,
                         suppress_callback_exceptions=False,
                         external_stylesheets=[dbc.themes.SUPERHERO],
                         external_scripts=None)

        app.layout = html.Div(children=[
            html.H1(
                'Override the `dash_ui` classproperty to create a Dash UI for '
                f'{cls._meta.verbose_name_plural}'),

            dcc.Dropdown(
                id='ai-model-dropdown',
                # (string; optional):
                # The ID of this component,
                # used to identify dash components in callbacks.
                # The ID needs to be unique across all of the app's components.

                className='dropdown',
                # (string; optional): className of the dropdown element.

                clearable=True,
                # (boolean; default True):
                # Whether or not the dropdown is "clearable",
                # that is, whether or not a small "x" appears on the right
                # of the dropdown that removes the selected value.

                disabled=False,
                # (boolean; default False):
                # If True, this dropdown is disabled and the selection
                # cannot be changed.

                loading_state=None,
                # (dict; optional):
                # Object that holds the loading state object
                # coming from dash-renderer.
                # loading_state is a dict with keys:
                # - component_name (string; optional):
                #     Holds the name of the component that is loading.
                # - is_loading (boolean; optional):
                #     Determines if the component is loading or not.
                # - prop_name (string; optional):
                #     Holds which property is loading.

                multi=False,
                # (boolean; default False):
                # If True, the user can select multiple values.

                optionHeight=48,
                # (number; default 35): height of each option.
                # Can be increased when label lengths would wrap around.

                options=[dict(disabled=False, label=i, title=i, value=i)
                         for i in cls.names_or_uuids],
                # (list of dicts; optional): An array of options
                # {label: [string|number], value: [string|number]},
                # an optional disabled field can be used for each option.
                # options is a list of dicts with keys:
                # - disabled (boolean; optional):
                #     If True, this option is disabled and cannot be selected.
                # - label (string | number; required): The dropdown's label.
                # - title (string; optional):
                #     The HTML 'title' attribute for the option.
                #     Allows for information on hover.
                #     For more information on this attribute, see
                # developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title.
                # - value (string | number; required):
                #     The value of the dropdown.
                #     This value corresponds to the items specified
                #     in the value property.

                persisted_props=['value'],
                # (list of values equal to: 'value'; default ['value']):
                # Properties whose user interactions will persist
                # after refreshing the component or the page. Since only value
                # is allowed this prop can normally be ignored.

                persistence=True,
                # (boolean | string | number; optional):
                # Used to allow user interactions in this component
                # to be persisted when the component - or the page -
                # is refreshed. If persisted is truthy and hasn't changed
                # from its previous value, a value that the user has changed
                # while using the app will keep that change,
                # as long as the new value also matches what was given
                # originally. Used in conjunction with persistence_type.

                persistence_type='session',
                # (a value equal to: 'local', 'session' or 'memory';
                # default 'local'):
                # Where persisted user changes will be stored:
                # - memory: only kept in memory, reset on page refresh.
                # - local: window.localStorage,
                #          data is kept after the browser quit.
                # - session: window.sessionStorage,
                #            data is cleared once the browser quit.

                placeholder='AI Model Name or UUID',
                # (string; optional):
                # The grey, default text shown when no option is selected.

                search_value=None,
                # (string; optional):
                # The value typed in the DropDown for searching.

                searchable=True,
                # (boolean; default True):
                # Whether to enable the searching feature or not.

                style=None,
                # (dict; optional):
                # Defines CSS styles which will override styles previously set.

                value=None,
                # (string | number | list of strings | numbers; optional):
                # The value of the input.
                # If multi is False (the default) then value is
                # just a string that corresponds to the values provided
                # in the options property.
                # If multi is True,
                # then multiple values can be selected at once,
                # and value is an array of items with values corresponding
                # to those in the options prop.
            ),

            html.Div(id='ai-model-dropdown-output-container'),
            ],   # noqa: E123
            # (list of or a singular dash component, string or number;
            # optional): The children of this component.

            # id=...,
            # (string; optional): The ID of this component,
            # used to identify dash components in callbacks.
            # The ID needs to be unique across all of the components in an app.

            accessKey=None,
            # (string; optional):
            # Keyboard shortcut to activate or add focus to the element.

            # aria-* (string; optional): A wildcard aria attribute.

            className=None,
            # (string; optional):
            # Often used with CSS to style elements with common properties.

            contentEditable=True,
            # (string; optional):
            # Indicates whether the element's content is editable.

            contextMenu=None,
            # (string; optional):
            # Defines the ID of a <menu> element
            # which will serve as the element's context menu.

            # data-* (string; optional): A wildcard data attribute.

            dir='ltr',
            # (string; optional): Defines the text direction.
            # Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left).

            draggable=True,
            # (string; optional): Defines whether the element can be dragged.

            hidden=False,
            # (a value equal to: 'hidden' or 'HIDDEN' | boolean; optional):
            # Prevents rendering of given element,
            # while keeping child elements, e.g. script elements, active.

            key=None,
            # (string; optional): A unique identifier for the component,
            # used to improve performance by React.js while rendering
            # components. See https://reactjs.org/docs/lists-and-keys.html
            # for more info.

            lang='en',
            # (string; optional): Defines the language used in the element.

            loading_state=None,
            # (dict; optional):
            # Object that holds the loading state object
            # coming from dash-renderer.
            # loading_state is a dict with keys:
            # - component_name (string; optional):
            #     Holds the name of the component that is loading.
            # - is_loading (boolean; optional):
            #     Determines if the component is loading or not.
            # - prop_name (string; optional):
            # Holds which property is loading.

            n_clicks=0,
            # (number; default 0):
            # An integer that represents the number of times that
            # this element has been clicked on.

            n_clicks_timestamp=-1,
            # (number; default -1):
            # An integer that represents the time (in ms since 1970)
            # at which n_clicks changed.
            # This can be used to tell which button was changed most recently.

            role=None,
            # (string; optional): The ARIA role attribute.

            spellCheck=True,
            # (string; optional):
            # Indicates whether spell checking is allowed for the element.

            style={'height': '88%', 'width': '88%'},
            # (dict; optional):
            # Defines CSS styles which will override styles previously set.

            tabIndex=None,
            # (string; optional):
            # Overrides the browser's default tab order and
            # follows the one specified instead.

            title=None
            # (string; optional):
            # Text to be displayed in a tooltip when hovering over the element.
        )

        @app.callback(Output(component_id='ai-model-dropdown-output-container',
                             component_property='children'),
                      Input(component_id='ai-model-dropdown',
                            component_property='value'))
        def update_ai_model_dropdown_output(value):
            return f'{value} selected' if value else None

        return app

    @classproperty
    def gradio_ui(cls) -> Interface:   # noqa: N805
        # pylint: disable=no-self-argument
        """Return the AIModel class's Gradio Interface."""
        return Interface(
            fn=cls.predict,
            # (Callable) - the function to wrap an interface around.

            inputs=[],
            # (Union[str, list[Union[str, InputComponent]]]) -
            # a single Gradio input component,
            # or list of Gradio input components.
            # Components can either be passed as instantiated objects,
            # or referred to by their string shortcuts.
            # The number of input components should match
            # the number of parameters in fn.

            outputs=JSONOutput(label='AI Model Output'),
            # (Union[str, list[Union[str, OutputComponent]]]) -
            # a single Gradio output component,
            # or list of Gradio output components.
            # Components can either be passed as instantiated objects,
            # or referred to by their string shortcuts.
            # The number of output components should match
            # the number of values returned by fn.

            verbose=True,
            # (bool) - whether to print detailed information during launch.

            examples=None,
            # (Union[list[list[Any]], str]) - sample inputs for the function;
            # if provided, appears below the UI components and can be used
            # to populate the interface.
            # Should be nested list, in which the outer list consists of
            # samples and each inner list consists of an input
            # corresponding to each input component.
            # A string path to a directory of examples can also be provided.
            # If there are multiple input components and a directory
            # is provided, a log.csv file must be present in the directory
            # to link corresponding inputs.

            examples_per_page=10,
            # (int) - If examples are provided, how many to display per page.

            live=False,
            # (bool) - should the interface automatically reload on change?

            layout='unaligned',
            # (str) - Layout of input and output panels.
            # - "horizontal" arranges them as two columns of equal height,
            # - "unaligned" arranges them as two columns of unequal height, and
            # - "vertical" arranges them vertically.

            show_input=True,
            show_output=True,

            capture_session=False,
            # (bool) - if True, captures the default graph and session
            # (needed for Tensorflow 1.x)

            interpretation='default',
            # (Union[Callable, str]) - function that provides interpretation
            # explaining prediction output.
            # Pass "default" to use built-in interpreter.

            num_shap=2.0,
            # (float) - a multiplier that determines how many examples
            # are computed for shap-based interpretation.
            # Increasing this value will increase shap runtime,
            # but improve results.

            theme='default',
            # (str) - Theme to use - one of
            # - "default",
            # - "huggingface",
            # - "grass",
            # - "peach".
            # Add "dark" prefix, e.g. "darkpeach" or "darkdefault"
            # for darktheme.

            repeat_outputs_per_model=True,

            title=cls._meta.verbose_name,
            # (str) - a title for the interface;
            # if provided, appears above the input and output components.

            description=('Cverride the `gradio_ui` classproperty to create a '
                         f'Gradio UI for {cls._meta.verbose_name_plural}'),
            # (str) - a description for the interface;
            # if provided, appears above the input and output components.

            article=None,
            # (str) - an expanded article explaining the interface;
            # if provided, appears below the input and output components.
            # Accepts Markdown and HTML content.

            thumbnail=None,
            # (str) - path to image or src to use as display picture for models
            # listed in gradio.app/hub

            css=None,
            # (str) - custom css or path to custom css file
            # to use with interface.

            server_port=None,
            # (int) - will start gradio app on this port (if available)

            # server_name=networking.LOCALHOST_NAME,
            # (str) - to make app accessible on local network set to "0.0.0.0".

            height=500,
            width=900,

            allow_screenshot=True,
            # (bool) - if False, users will not see a button
            # to take a screenshot of the interface.

            allow_flagging=False,
            # (bool) - if False, users will not see a button
            # to flag an input and output.

            flagging_options=None,
            # (list[str]) - if not None, provides options a user must select
            # when flagging.

            encrypt=False,
            # (bool) - If True, flagged data will be encrypted
            # by key provided by creator at launch

            show_tips=False,
            # (bool) - if True, will occasionally show tips
            # about new Gradio features

            flagging_dir='flagged',
            # (str) - what to name the dir where flagged data is stored.

            analytics_enabled=True,

            enable_queue=False,
            # (bool) - if True, inference requests will be served through
            # a queue instead of with parallel threads.
            # Required for longer inference times (> 1min) to prevent timeout.
        )


class _AIModelWithArtifactFilesABC(AIModel):
    artifact_global_url: CharField = \
        CharField(
            verbose_name='Model Artifact Global URL',
            help_text='Model Artifact Global URL',

            max_length=255,

            null=True,
            blank=True,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages={},
            primary_key=False,
            unique=True,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    artifact_local_path: CharField = \
        CharField(
            verbose_name='Model Artifact Local Path',
            help_text='Model Artifact Local Path',

            max_length=255,

            null=True,
            blank=True,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages={},
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    native_obj: Optional[Any] = None

    class Meta(AIModel.Meta):   # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True

    @abstractmethod
    def load(self) -> None:
        """Load the Model's native object from its artifact file(s)."""
        raise NotImplementedError

    def unload(self) -> None:
        """Unload the Model's native object to free up memory."""
        self.native_obj = None
