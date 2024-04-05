import weaviate

client = weaviate.connect_to_custom(
    http_host="weaviate",
    http_port="80",
    http_secure=False,
    grpc_host="weaviate-grpc",
    grpc_port="50051",
    grpc_secure=False,
    # headers={
    #     "X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")  # Or any other inference API keys
    # }
)

client.is_ready()
# True

client.is_live()
# True

from weaviate.classes.config import Property, DataType

client.collections.create(
    "Article",
    properties=[
        Property(name="title", data_type=DataType.TEXT),
        Property(name="body", data_type=DataType.TEXT),
    ]
)

client.collections.list_all()

# {'Article': _CollectionConfigSimple(name='Article', description=None, generative_config=None, properties=[_Property(name='title', description=None, data_type=<DataType.TEXT: 'text'>, index_filterable=True, index_searchable=True, nested_properties=None, tokenization=<Tokenization.WORD: 'word'>, vectorizer_config=None, vectorizer='none'), _Property(name='body', description=None, data_type=<DataType.TEXT: 'text'>, index_filterable=True, index_searchable=True, nested_properties=None, tokenization=<Tokenization.WORD: 'word'>, vectorizer_config=None, vectorizer='none')], references=[], reranker_config=None, vectorizer_config=None, vectorizer=<Vectorizers.NONE: 'none'>, vector_config=None)}

client.close()