#!/usr/bin/python3

import requests
import json
import click
from pprint import pprint

#Get api key.
with open("api-key.txt") as f:
  apiKey = f.readline().rstrip()

#Establish the base url and headers.
base = "https://yfapi.net"
headers = {"x-api-key": apiKey}

#Establish a group.
@click.group()
def cli():
  """
  Command-line implementation of yahoofinanceapi.com
  """
  pass

@click.command()
@click.argument("symbols", required=True)
@click.option("--lang", type=click.Choice(["en", "fr", "de", "it", "es", "zh"]), default="en" )
@click.option("--region", type=click.Choice(["US", "AU", "CA", "FR", "DE", "HK", "IT", "ES", "GB", "IN"]), default="US" )
@click.option("--debug", is_flag=True)
def quote(symbols, lang, region, debug):
  """
  [--lang LANG] [--region REGION] [--debug] SYMBOLS 
  """

  #Create a query string to accomodate url parameters; establish a route as per the api.
  querystring = {"symbols": symbols, "lang": lang, "region": region}
  quoteRoute = "/v6/finance/quote"
  url = f"{base}{quoteRoute}"

  #Print debug info if debug flag is set.
  if(debug):
    print("Making a request of the quote route...")
    print(f"URL:  {url}\n\n")

  #Make get request.
  r = requests.get(url, headers=headers, params=querystring)
  output = json.loads(r.text)
  pprint(output)
  return output


@click.command()
@click.argument("ticker", required=True)
@click.option("--rang", type=click.Choice(["1d", "5d", "1mo", "3mo", "6mo", "1yr", "5yr", "10yr", "ytd", "max"]), default="1mo")
@click.option("--region", type=click.Choice(["US", "AU", "CA", "FR", "DE", "HK", "IT", "ES", "GB", "IN"]), default="US" )
@click.option("--interval", type=click.Choice(["1m", "5m", "15m", "1d", "1wk", "1mo"]), default="1d")
@click.option("--lang", type=click.Choice(["en", "fr", "de", "it", "es", "zh"]), default="en" )
@click.option("--debug", is_flag=True)
def chart(ticker, rang, region, interval, lang, debug):
  """
  [--rang RANG] [--region REGION] [--interval INTERVAL] [--lang LANG] [--debug] TICKER
  """

  #Create a query string to accomodate url parameters; establish a route as per the api.
  chartRoute = "/v8/finance/chart/"
  url = f"{base}{chartRoute}{ticker}"
  querystring = {"range": rang, "region": region, "interval": interval, "lang": lang}

  #Print debugging statements if the debug flag is set to true.
  if(debug):
    print("Making a request of the chart route...")
    print(f"URL:  {url}\n\n")

  #Make and format the request.
  r = requests.get(url, headers=headers, params=querystring)
  output = json.loads(r.text)
  pprint(output)
  return output


@click.command()
@click.argument("symbol", required=True)
@click.option("--date", type=int)
@click.option("--debug", is_flag=True)
def options(symbol, date, debug):
  """
  [--date DATE] [--debug] SYMBOL 
  """

  #Create a query string to accomodate url parameters; establish a route as per the api.
  optionsRoute = "/v7/finance/options/"
  url = f"{base}{optionsRoute}{symbol}"
  querystring={"date": date}

  #Print debugging statements if the debug flag is set to true.
  if(debug):
    print("Making a request of the options route...")
    print(f"URL:  {url}\n\n")

  #Make and format the request.
  r = requests.get(url, headers=headers, params=querystring)
  output = json.loads(r.text)
  pprint(output)
  return output


@click.command()
@click.argument("symbols", required=True)
@click.option("--interval", type=click.Choice(["1m", "5m", "15m", "1d", "1wk", "1mo"]), default="1d")
@click.option("--rang", type=click.Choice(["1d", "5d", "1mo", "3mo", "6mo", "1yr", "5yr", "10yr", "ytd", "max"]), default="1mo")
@click.option("--debug", is_flag=True)
def spark(symbols, interval, rang, debug):
  """
  [--interval INTERVAL] [--rang RANG] [--debug] SYMBOLS
  """

  #Create a query string to accomodate url parameters; establish a route as per the api.
  sparkRoute = "/v8/finance/spark"
  url = f"{base}{sparkRoute}"
  querystring = {"symbols": symbols, "interval": interval, "range": rang}

  #Print debugging statements if the debug flag is set to true.
  if(debug):
    print("Making a request of the spark route...")
    print(f"URL:  {url}\n\n")

  #Make and format the request.
  r = requests.get(url, headers=headers, params=querystring)
  output = json.loads(r.text)
  pprint(output)
  return output


@click.command()
@click.argument("symbol", required=True)
@click.option("--debug", is_flag=True)
def recommendations(symbol, debug):
  """
  [--debug] SYMBOL
  """

  #Establish the route as per the api.
  recommendationsRoute = "/v6/finance/recommendationsbysymbol/"
  url = f"{base}{recommendationsRoute}{symbol}"

  #Print debugging statements if the debug flag is set to true.
  if(debug):
    print("Making a request of the recommendations route...")
    print(f"URL:  {url}\n\n")

  #Make and format the request.
  r = requests.get(url, headers=headers)
  output = json.loads(r.text)
  pprint(output)
  return output


@click.command()
@click.argument("symbol", required=True)
@click.option("--debug", is_flag=True)
def insights(symbol, debug):
  """
  [--debug] SYMBOL
  """

  #Create a query string to accomodate url parameters; establish a route as per the api.
  insightsRoute = "/ws/insights/v1/finance/insights"
  url = f"{base}{insightsRoute}"
  querystring = {"symbol": symbol}

  #Print debugging statements if the debug flag is set to true.
  if(debug):
    print("Making a request of the insights route...")
    print(f"URL:  {url}\n\n")

  #Make and format the request.
  r = requests.get(url, headers=headers, params=querystring)
  output = json.loads(r.text)
  pprint(output)
  return output


@click.command()
@click.argument("query", required=True)
@click.option("--region", type=click.Choice(["US", "AU", "CA", "FR", "DE", "HK", "IT", "ES", "GB", "IN"]), default="US" )
@click.option("--lang", type=click.Choice(["en", "fr", "de", "it", "es", "zh"]), default="en" )
@click.option("--debug", is_flag=True)
def autocomplete(query, region, lang, debug):
  """
  [--region REGION] [--lang LANG] [--debug] QUERY
  """

  #Create a query string to accomodate url parameters; establish a route as per the api.
  autocompleteRoute = "/v6/finance/autocomplete"
  url = f"{base}{autocompleteRoute}"
  querystring = {"query": query, "lang": lang, "region": region}

  #Print debugging statements if the debug flag is set to true.
  if(debug):
    print("Making a request of the autocomplete route...")
    print(f"URL:  {url}\n\n")

  #Make and format the request.
  r = requests.get(url, headers=headers, params=querystring)
  output = json.loads(r.text)
  pprint(output)
  return output


@click.command()
@click.option("--lang", type=click.Choice(["en", "fr", "de", "it", "es", "zh"]), default="en" )
@click.option("--region", type=click.Choice(["US", "AU", "CA", "FR", "DE", "HK", "IT", "ES", "GB", "IN"]), default="US" )
@click.option("--debug", is_flag=True)
def market_summary(lang, region, debug):
  """
  [--lang LANG] [--region REGION] [--debug]
  """

  #Create a query string to accomodate url parameters; establish a route as per the api.
  summaryRoute = "/v6/finance/quote/marketSummary"
  url = f"{base}{summaryRoute}"
  querystring = {"lang": lang, "region": region}

  #Print debugging statements if the debug flag is set to true.
  if(debug):
    print("Making a request of the maket summary route...")
    print(f"URL:  {url}\n\n")

  #Make and format the request.
  r = requests.get(url, headers=headers, params=querystring)
  output = json.loads(r.text)
  pprint(output)
  return output


@click.command()
@click.option("--region", type=click.Choice(["US", "AU", "CA", "FR", "DE", "HK", "IT", "ES", "GB", "IN"]), default="US" )
@click.option("--debug", is_flag=True)
def region(region, debug):
  """
  [--region REGION] [--debug]
  """

  #Establish the route as per the api.
  regionRoute = "/v1/finance/trending/"
  url = f"{base}{regionRoute}{region}"

  #Print debugging statements if the debug flag is set to true.
  if(debug):
    print("Making a request of the region route...")
    print(f"URL:  {url}\n\n")

  #Make and format the request.
  r = requests.get(url, headers=headers)
  output = json.loads(r.text)
  pprint(output)
  return output


#Add the individual functions to the cli group.
cli.add_command(quote)
cli.add_command(chart)
cli.add_command(options)
cli.add_command(spark)
cli.add_command(recommendations)
cli.add_command(insights)
cli.add_command(autocomplete)
cli.add_command(market_summary)
cli.add_command(region)


if __name__ == "__main__":
  cli()
