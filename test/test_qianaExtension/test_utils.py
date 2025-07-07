def test_next_quoted_var():
    from qiana.qianaExtension.tptpUtils import next_quoted_var

    # Test with an empty list
    try:
        next_quoted_var([], -1)
        assert False, "Expected ValueError for negative nbr_vars with empty list"
    except ValueError as e: pass

    # Test with a single variable
    assert next_quoted_var(["q_X1"]) == "q_X2"

    # Test with multiple variables
    assert next_quoted_var(["q_X1", "q_X2", "q_X3"], 2) == ["q_X4", "q_X5"]
    assert next_quoted_var(["q_X1", "q_X2", "q_X3"], 1) == "q_X4"