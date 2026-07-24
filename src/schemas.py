# this file will store schemas for all the endpoints that we will be receiving through the API

from pyspark.sql.types import *

# products schema
products_schema = StructType([

    StructField("id", IntegerType(), True),
    StructField("title", StringType(), True),
    StructField("description", StringType(), True),
    StructField("category", StringType(), True),

    StructField("price", DoubleType(), True),
    StructField("discountPercentage", DoubleType(), True),
    StructField("rating", DoubleType(), True),

    StructField("stock", IntegerType(), True),

    StructField(
        "tags",
        ArrayType(StringType()),
        True
    ),

    StructField("brand", StringType(), True),
    StructField("sku", StringType(), True),

    StructField("weight", IntegerType(), True),

    StructField(
        "dimensions",
        StructType([
            StructField("width", DoubleType(), True),
            StructField("height", DoubleType(), True),
            StructField("depth", DoubleType(), True)
        ]),
        True
    ),

    StructField("warrantyInformation", StringType(), True),
    StructField("shippingInformation", StringType(), True),
    StructField("availabilityStatus", StringType(), True),

    StructField(
        "reviews",
        ArrayType(
            StructType([
                StructField("rating", IntegerType(), True),
                StructField("comment", StringType(), True),
                StructField("date", StringType(), True),
                StructField("reviewerName", StringType(), True),
                StructField("reviewerEmail", StringType(), True)
            ])
        ),
        True
    ),

    StructField("returnPolicy", StringType(), True),
    StructField("minimumOrderQuantity", IntegerType(), True),

    StructField(
        "meta",
        StructType([
            StructField("createdAt", StringType(), True),
            StructField("updatedAt", StringType(), True),
            StructField("barcode", StringType(), True),
            StructField("qrCode", StringType(), True)
        ]),
        True
    ),

    StructField(
        "images",
        ArrayType(StringType()),
        True
    ),

    StructField("thumbnail", StringType(), True)

])

# carts schema
carts_schema = StructType([

    StructField("id", IntegerType(), True),

    StructField(
        "products",
        ArrayType(
            StructType([
                StructField("id", IntegerType(), True),
                StructField("title", StringType(), True),
                StructField("price", DoubleType(), True),
                StructField("quantity", IntegerType(), True),
                StructField("total", DoubleType(), True),
                StructField("discountPercentage", DoubleType(), True),
                StructField("discountedTotal", DoubleType(), True),
                StructField("thumbnail", StringType(), True)
            ])
        ),
        True
    ),

    StructField("total", DoubleType(), True),
    StructField("discountedTotal", DoubleType(), True),
    StructField("userId", IntegerType(), True),
    StructField("totalProducts", IntegerType(), True),
    StructField("totalQuantity", IntegerType(), True)

])

# users schema
users_schema = StructType([

    StructField("id", IntegerType(), True),
    StructField("firstName", StringType(), True),
    StructField("lastName", StringType(), True),
    StructField("maidenName", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("gender", StringType(), True),
    StructField("email", StringType(), True),
    StructField("phone", StringType(), True),
    StructField("username", StringType(), True),
    StructField("password", StringType(), True),
    StructField("birthDate", StringType(), True),
    StructField("image", StringType(), True),
    StructField("bloodGroup", StringType(), True),
    StructField("height", FloatType(), True),
    StructField("weight", FloatType(), True),
    StructField("eyeColor", StringType(), True),

    StructField(
        "hair",
        StructType([
            StructField("color", StringType(), True),
            StructField("type", StringType(), True)
        ]),
        True
    ),

    StructField("ip", StringType(), True),

    StructField(
        "address",
        StructType([
            StructField("address", StringType(), True),
            StructField("city", StringType(), True),
            StructField("state", StringType(), True),
            StructField("stateCode", StringType(), True),
            StructField("postalCode", StringType(), True),
            StructField(
                "coordinates",
                StructType([
                    StructField("lat", FloatType(), True),
                    StructField("lng", FloatType(), True)
                ]),
                True
            ),
            StructField("country", StringType(), True)
        ]),
        True
    ),

    StructField("macAddress", StringType(), True),
    StructField("university", StringType(), True),

    StructField(
        "bank",
        StructType([
            StructField("cardExpire", StringType(), True),
            StructField("cardNumber", StringType(), True),
            StructField("cardType", StringType(), True),
            StructField("currency", StringType(), True),
            StructField("iban", StringType(), True)
        ]),
        True
    ),

    StructField(
        "company",
        StructType([
            StructField("department", StringType(), True),
            StructField("name", StringType(), True),
            StructField("title", StringType(), True),
            StructField(
                "address",
                StructType([
                    StructField("address", StringType(), True),
                    StructField("city", StringType(), True),
                    StructField("state", StringType(), True),
                    StructField("stateCode", StringType(), True),
                    StructField("postalCode", StringType(), True),
                    StructField(
                        "coordinates",
                        StructType([
                            StructField("lat", FloatType(), True),
                            StructField("lng", FloatType(), True)
                        ]),
                        True
                    ),
                    StructField("country", StringType(), True)
                ]),
                True
            )
        ]),
        True
    ),

    StructField("ein", StringType(), True),
    StructField("ssn", StringType(), True),
    StructField("userAgent", StringType(), True),

    StructField(
        "crypto",
        StructType([
            StructField("coin", StringType(), True),
            StructField("wallet", StringType(), True),
            StructField("network", StringType(), True)
        ]),
        True
    ),

    StructField("role", StringType(), True)

])

# posts schema
posts_schema = StructType([

    StructField("id", IntegerType(), True),
    StructField("title", StringType(), True),
    StructField("body", StringType(), True),

    StructField(
        "tags",
        ArrayType(StringType()),
        True
    ),

    StructField(
        "reactions",
        StructType([
            StructField("likes", IntegerType(), True),
            StructField("dislikes", IntegerType(), True)
        ]),
        True
    ),

    StructField("views", IntegerType(), True),
    StructField("userId", IntegerType(), True)

])

# comments schema
comments_schema = StructType([

    StructField("id", IntegerType(), True),
    StructField("body", StringType(), True),

    StructField("postId", IntegerType(), True),
    StructField("likes", IntegerType(), True),

    StructField(
        "user",
        StructType([
            StructField("id", IntegerType(), True),
            StructField("username", StringType(), True),
            StructField("fullName", StringType(), True)
        ]),
        True
    )

])

# quotes schema
quotes_schema = StructType([

    StructField("id", IntegerType(), True),
    StructField("quote", StringType(), True),
    StructField("author", StringType(), True)

])

# todos schema
todos_schema = StructType([

    StructField("id", IntegerType(), True),
    StructField("todo", StringType(), True),
    StructField("completed", BooleanType(), True),
    StructField("userId", IntegerType(), True)

])

# recipes schema
recipes_schema = StructType([

    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),

    StructField(
        "ingredients",
        ArrayType(StringType()),
        True
    ),

    StructField(
        "instructions",
        ArrayType(StringType()),
        True
    ),

    StructField("prepTimeMinutes", IntegerType(), True),
    StructField("cookTimeMinutes", IntegerType(), True),
    StructField("servings", IntegerType(), True),

    StructField("difficulty", StringType(), True),
    StructField("cuisine", StringType(), True),

    StructField("caloriesPerServing", IntegerType(), True),

    StructField(
        "tags",
        ArrayType(StringType()),
        True
    ),

    StructField("userId", IntegerType(), True),
    StructField("image", StringType(), True),

    StructField("rating", DoubleType(), True),
    StructField("reviewCount", IntegerType(), True),

    StructField(
        "mealType",
        ArrayType(StringType()),
        True
    )

])

ENDPOINT_SCHEMAS = {
    'products': products_schema,
    'carts': carts_schema,
    'users': users_schema,
    'posts': posts_schema,
    'comments': comments_schema,
    'quotes': quotes_schema,
    'todos': todos_schema,
    'recipes': recipes_schema
}