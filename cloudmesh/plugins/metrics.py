import sys
try:
    from fgmetric.shell.FGMetricAPI import FGMetricAPI
except:
    print "fgmetric module not found"

class MetricsPlugin:

    def __init__(self):
        self.api = FGMetricAPI()
        self.metrics = None

    def get_userlist(self):
        """get list of userinfo"""
        if not self.api:
            return

        userlist = self.api.get_userinfo()
        self.userlist = sorted(userlist, key = lambda t:
                               str(t["first_name"]).lower())
        return self.userlist

    def get_instances(self):
        """Get list of instances
        Args:
            args(dict): including a user id
        """
        if not self.api:
            return

        return self.api.get_instances()

    def get(self, args):
        """Get usage data from FG Metrics"""

        if not self.api:
            return

        try:
            args["user"] = args["user"] or self.user
            self._set_api_vars(args)
            # print args
            stats = self.api._set_dict_vars()
            metrics = self.api.get_stats()
            stats["stats"] = metrics
            self.metrics = stats
            # print self.metrics
        except:
            print sys.exc_info()
            pass
        return self.metrics

    def get_realtime(self, args):
        """ get real-time usage data from FG Metrics"""

        # IN DEVELOPMENT
        if not self.api:
            return

        try:
            print 1#

        except:
            pass

    def _set_api_vars(self, args):
        self.api.set_date(args["s_date"], args["e_date"])
        self.api.set_metric(
            "count runtime cores mem disks")  # args["metric"])
        self.api.set_user(args["user"])
        self.api.set_cloud(args["cloud"])
        self.api.set_hostname(args["host"])
        self.api.set_period(args["period"])

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


