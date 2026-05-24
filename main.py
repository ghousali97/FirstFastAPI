def main():
    """Run the FastAPI app with uvicorn when executed as a script.

    Note: this requires the project dependencies (fastapi, uvicorn) to be installed.
    """
    try:
        import uvicorn

        uvicorn.run("books:app", host="127.0.0.1", port=8000, log_level="info")
    except Exception:
        # Fallback to a print message if uvicorn isn't available in the environment.
        print("uvicorn is not installed. Install dependencies to run the server: pip install -r requirements.txt")


if __name__ == "__main__":
    main()
