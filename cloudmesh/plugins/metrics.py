try:
    from fgmetric.FGMetricsAPI import FGMetricsAPI
except:
    print "fgmetric module not found"

class MetricsPlugin:

    def __init__(self):
        self.metric_api = FGMetricsAPI()

    def get_metrics_cli(self, args):
        """ Get usage data from FG Metric CLI"""
        """ This is replica with get_metrics but using CLI instead of API """
        """
        Args:
            args (dict): parameters for CLI with option
        Return:
            (dict): output of fgmetric in a dict type
        Raise:
            n/a
        """
        try:
            res = fgmetric(args) # args should be list-lized before send it out
            return json.loads(res, object_hook=json_util.object_hook)
        except:
            pass

    def get_metrics(self, args):
        """Get usage data from FG Metrics"""

        if not self.metric_api:
            return

        try:
            args["user"] = args["user"] or self.user
            self._set_metric_api_vars(args)
            # print args
            stats = self.metric_api._set_dict_vars()
            metrics = self.metric_api.get_stats()
            stats["stats"] = metrics
            self.metrics = stats
            # print self.metrics
        except:
            print sys.exc_info()
            pass
        return self.metrics

    def get_realtime_metrics(self, args):
        """ get real-time usage data from FG Metrics"""

        # IN DEVELOPMENT
        if not self.metric_api:
            return

        try:
            print 1#

        except:
            pass

    def _set_metric_api_vars(self, args):
        self.metric_api.set_date(args["s_date"], args["e_date"])
        self.metric_api.set_metric(
            "count runtime cores mem disks")  # args["metric"])
        self.metric_api.set_user(args["user"])
        self.metric_api.set_cloud(args["cloud"])
        self.metric_api.set_hostname(args["host"])
        self.metric_api.set_period(args["period"])

