clean:
	rm -rv __pycache__ || echo "Cache files cleaned"
	rm -rv .pytest_cache || echo "Test files cleaned"
