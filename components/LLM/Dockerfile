FROM ollama/ollama:0.1.34

# Copy the start script and make it executable
COPY start-ollama.sh ./
RUN chmod +x ./start-ollama.sh

# Expose the Ollama port
EXPOSE 11434

ENTRYPOINT ./start-ollama.sh
# CMD ["/bin/ollama", "pull", "mistral-small"]
# CMD ["echo", "Hello, World!"]