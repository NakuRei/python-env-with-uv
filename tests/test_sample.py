"""Sample test file."""

from python_env_with_uv.sample import hello


class TestSample:
    """Test class for Sample module."""

    def test_hello(self) -> None:
        """Test the hello function."""
        assert hello() == "Hello from Sample module!"
