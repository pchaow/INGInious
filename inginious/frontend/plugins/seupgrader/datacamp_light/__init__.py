#SEUP DATACAMP JS

def javascript_footer() :
    return "//cdn.datacamp.com/dcl-react.js.gz"
    


def init(plugin_manager, course_factory, client, plugin_config):
    """ Init the plugin """
    plugin_manager.add_hook("javascript_footer", javascript_footer
)
