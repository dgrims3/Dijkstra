class Vertex:
    # Areas of this code are paraphrased from (Lysecky et al., 2018)
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None

    # Overload method that prints the vertex label as a string.
    def __str__(self):
        return "%s" % self.label