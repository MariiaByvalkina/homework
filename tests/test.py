import pytest

from dfs import Graph

def test_single_vertex():
    graph = Graph([1], [])
    assert graph.dfs() == [1]

def test_two_connected_vertices():
    graph = Graph([1, 2], [(1, 2)])
    result = graph.dfs()
    assert len(result) == 2
    assert 1 in result
    assert 2 in result

def test_three_vertices_chain():
    graph = Graph([1, 2, 3], [(1, 2), (2, 3)])
    result = graph.dfs()
    assert result == [1, 2, 3]

def test_iteration():
    graph = Graph([1, 2, 3], [(1, 2), (2, 3)])
    visited = list(graph)
    assert visited == graph.dfs()

def test_disconnected_components():
    graph = Graph([1, 2, 3, 4], [(1, 2), (3, 4)])
    result = graph.dfs()
    assert len(result) == 4
    assert set(result) == {1, 2, 3, 4}
