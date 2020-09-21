import graphene
from graphene_django import DjangoObjectType

from ingredients.models import Category, Ingredient


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")


# class CategoryInput(graphene.InputObjectType):
#     name = graphene.String(required=True)
#     pass

class CreateCategory(graphene.Mutation):
    ok = graphene.Boolean()
    status = graphene.String()

    class Input:
        name = graphene.String(required=True)

    # cat = graphene.Field(lambda: CategoryType)

    @staticmethod
    def mutate(self, info, name):
        c = Category.objects.create(name=name)
        return {"ok": True, "status": "Created successfully"}


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    all_categories = graphene.List(CategoryType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    @staticmethod
    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    @staticmethod
    def resolve_all_categories(root, info):
        # print(info.context.user)
        return Category.objects.all()

    @staticmethod
    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query, mutation=Mutation)
