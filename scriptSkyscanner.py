import requests

def getJsonSkyScanner(headers,origen, destino, fecha):
    country = "ES"
    currency = "EUR"
    locale = "es-ES"

    params = "/".join([country, currency, locale, origen, destino, fecha])

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/" + params

    querystring = {"inboundpartialdate": "2021-03-28"}

    return requests.request("GET", url, headers=headers, params=querystring).json()

def createTable(json):

    precios = json['Quotes']
    companias = json['Carriers']
    lugares = json['Places']

    for precio in precios:
        total = precio['MinPrice']
        for out in precio['OutboundLeg']['CarrierIds']:
            for compania in companias:
                if compania["CarrierId"] == out:
                    companiaName = compania["Name"]
            origen = [place for place in lugares if place['PlaceId'] == precio['OutboundLeg']['OriginId']][0]['Name']
            destino = [place for place in lugares if place['PlaceId'] == precio['OutboundLeg']['DestinationId']][0][
                'Name']
        fecha = precio['OutboundLeg']['DepartureDate']

        print(companiaName, origen, destino, fecha, total)


origen = "MAD-sky"
destino =["MVD-sky", "anywhere"]
fecha = "2021-02-28"


json = getJsonSkyScanner(origen, destino[0], fecha)

print(json)