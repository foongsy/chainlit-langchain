# Chainlit + Langchain + Claude 3 on Google Vertex e.g.

> This material is intended for Venturenix LLM course, use it at your own risk.

## Read before running
- Make sure the service account json path/name is matched

## Process to build Docker image
- Create `Dockerfile`
- Make sure to use `ENTRYPOINT` instead of `CMD`
- Build Image:
`docker build -t [image_name]:[tagname] .`
- Run Image:
`docker run -p 8000:8080 [image_name]:[tagname]`


## How to deploy to Google Cloud Run
- [Read the instruction and install gcloud cli](https://cloud.google.com/sdk/gcloud)
```
# Login with the account associated with GCP project
gcloud auth login
# Set vtxclass as default project
gcloud config set project vtxclass
# Login again to make this account as default for all GCP services
gcloud auth application-default login
# Once the dockrun is successful, you can try deploying to Google Cloud Run using following command
gcloud run deploy --source .
```

### References
- https://python.langchain.com/v0.1/docs/integrations/llms/google_vertex_ai_palm/#anthropic-on-vertex-ai
- https://api.python.langchain.com/en/latest/model_garden/langchain_google_vertexai.model_garden.ChatAnthropicVertex.html#langchain_google_vertexai.model_garden.ChatAnthropicVertex
- https://api.python.langchain.com/en/latest/llms/langchain_google_vertexai.llms.VertexAI.html#langchain_google_vertexai.llms.VertexAI
- https://cloud.google.com/docs/authentication/application-default-credentials#GAC
