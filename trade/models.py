from django.db import models
class Quotes_Name(models.Model):
  """This model for post in our blog"""
  name = models.TextField()
  def __str__(self):
    return self.name
 
class Quote(models.Model):
  """This model for Quotes"""
  date_time = models.DateTimeField(auto_now_add=True)
  q_open = models.FloatField(max_length=120)
  q_high = models.FloatField(max_length=120)
  q_low = models.FloatField(max_length=120)
  q_close = models.FloatField(max_length=120)
  q_adj_close = models.FloatField(max_length=120)
  q_volume = models.FloatField(max_length=120)
  q_name=models.ForeignKey(
    Quotes_Name,
    on_delete=models.CASCADE,
    default='1'
  )
 
import django_tables2 as tables
class QuoteTable(tables.Table):
    class Meta:
        model = Quote
        attrs = {'class': 'table table-hover table-sm'
        }

# import django_filters as df
# class QuoteFilter(df.FilterSet):
#     class Meta:
#         model = Quote
#         fields = ('date_time', 'q_open', )


# from django_filters.views import FilterView
# from django_tables2.views import SingleTableMixin
# class FilteredQuoteListView(SingleTableMixin, FilterView):
#     table_class = QuoteTable
#     model = Quote
#     template_name = "quotes_table.html"
#     filterset_class = QuoteFilter