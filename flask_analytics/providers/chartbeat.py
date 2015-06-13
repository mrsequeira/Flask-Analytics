from flask_analytics.providers.base import BaseProvider


class Chartbeat(BaseProvider):

    uid = None
    domain = None
    enabled = True

    def __init__(self, uid=None, domain=None, enabled=True):
        self.uid = uid
        self.domain = domain
        self.enabled = enabled

    @property
    def template(self):
        return """<script type="text/javascript">
    var _sf_async_config={{}};
    /** CONFIGURATION START **/
    _sf_async_config.uid = {uid}; /** CHANGE THIS **/
    _sf_async_config.domain = "{domain}"; /** CHANGE THIS **/
    /** CONFIGURATION END **/
    (function(){{
        function loadChartbeat() {{
            window._sf_endpt=(new Date()).getTime();
            var e = document.createElement("script");
            e.setAttribute("language", "javascript");
            e.setAttribute("type", "text/javascript");
            e.setAttribute('src', '//static.chartbeat.com/js/chartbeat.js');
            document.body.appendChild(e);
        }}
        var oldonload = window.onload;
        window.onload = (typeof window.onload != "function") ?
        loadChartbeat : function() {{ oldonload(); loadChartbeat(); }};
    }})();
</script>"""

    def __str__(self):
        if self.enabled:
            return self.template.format(uid=self.uid, domain=self.domain)
        else:
            return ''