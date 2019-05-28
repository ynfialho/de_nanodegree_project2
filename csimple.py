from cassandra.cluster import Cluster
import constants

class cassandraSimple:
    def __init__(self):
        self.cluster = Cluster(constants.CLUSTER_IP)
        self.session = self.connect()