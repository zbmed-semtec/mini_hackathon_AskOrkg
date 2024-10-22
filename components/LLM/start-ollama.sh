#!/bin/bash

# # Serve OLLaMA
/bin/ollama serve &

# # Sleep a bit to make sure it started
sleep 10

# Pull model
/bin/ollama pull mistral-small

# # Run model
# /bin/ollama run mistral-small

# Keep the container running
sleep infinity
