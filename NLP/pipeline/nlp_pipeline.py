from pipeline.nodes.PipelineNode import PipelineNode


class NLPPipeline:
    def __init__(self, first_input: str):
        self.__nodes = []
        self.__first_input = first_input

    def add(self, node: PipelineNode):
        self.__nodes.append(node)

    def run(self):
        output = self.__nodes[0].handle(self.__first_input)
        del self.__nodes[0]
        for node in self.__nodes:
            output = node.handle(output)
