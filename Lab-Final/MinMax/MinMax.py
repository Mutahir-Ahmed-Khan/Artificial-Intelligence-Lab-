import math


class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmaxValue = None


class MinMaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulateGoal(self, node):
        if node.minmaxValue is not None:
            return "Goal Reached"
        return "Searching"

    def act(self, environment, node):
        goalStatus = self.formulateGoal(node)

        if goalStatus == "Goal Reached":
            return node.minmaxValue
        else:
            return environment.computeMinMax(node, self.depth)


class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.visitedNodes = []

    def getPercept(self, node):
        return node

    def computeMinMax(self, node, depth, maxPlayer=True):

        if depth == 0 or not node.children:
            self.visitedNodes.append(node)
            return node.value

        if maxPlayer:
            value = -math.inf
            for child in node.children:
                childValue = self.computeMinMax(child, depth - 1, False)
                value = max(value, childValue)

            node.minmaxValue = value
            self.visitedNodes.append(node)
            return value

        else:
            value = math.inf
            for child in node.children:
                childValue = self.computeMinMax(child, depth - 1, True)
                value = min(value, childValue)

            node.minmaxValue = value
            self.visitedNodes.append(node)
            return value


def runAgent(agent, environment, startNode):
    percept = environment.getPercept(startNode)
    return agent.act(environment, percept)
