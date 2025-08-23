from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import ProductInventory


@registry.register_document
class ProductInventoryDocument(Document):

    # forign key
    product = fields.ObjectField(
        properties={
            "name": fields.TextField(),
        }
    )

    # reverse key
    product_inventory = fields.ObjectField(
        properties={
            "units": fields.IntegerField(),
        }
    )

    class Index:
        name = "productinventory"

    class Django:
        model = ProductInventory
        fields = [
            "id",
            "sku",
        ]


# Test Fetch

# curl -X GET "localhost:9200/_search?pretty" -H 'Content-Type: application/json' -d '
# {
#     "query":{
#             "bool":{
#                     "must":[
#                             {"match":{"sku": "7633969397"}}
#                     ]
#             }
#     }
# }'

# curl -X GET "localhost:9200/productinventory/_doc/1?pretty"
