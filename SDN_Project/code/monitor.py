from pox.core import core
import pox.openflow.libopenflow_01 as of
import time

log = core.getLogger()

class NetworkMonitor(object):
    def __init__(self):
        self.last_bytes = {}
        self.last_time = time.time()

        core.openflow.addListeners(self)

        # Start periodic stats request
        core.callDelayed(2, self._request_stats)

        log.info("🚀 Network Utilization Monitor Started")

    def _request_stats(self):
        for connection in core.openflow._connections.values():
            connection.send(of.ofp_stats_request(
                body=of.ofp_flow_stats_request()
            ))

        core.callDelayed(2, self._request_stats)

    def _handle_FlowStatsReceived(self, event):
        log.info("📊 ---- FLOW STATS ----")

        current_time = time.time()
        delta_time = current_time - self.last_time

        if delta_time == 0:
            return

        for stat in event.stats:
            if stat.match.nw_src is None or stat.match.nw_dst is None:
                continue

            key = (stat.match.nw_src, stat.match.nw_dst)

            old_bytes = self.last_bytes.get(key, 0)
            new_bytes = stat.byte_count

            # Calculate bandwidth (bits per second)
            bandwidth = (new_bytes - old_bytes) * 8 / delta_time

            print(f"Flow {key} | Bytes={new_bytes} | Bandwidth={bandwidth:.2f} bps")

            self.last_bytes[key] = new_bytes

        self.last_time = current_time

def launch():
    core.registerNew(NetworkMonitor)monitor.py