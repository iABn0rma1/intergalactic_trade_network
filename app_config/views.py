from django.shortcuts import render

def api_index(request):
    api_urls = [
        {'name': 'Initiate Trade', 'url': '/api/trades/'},
        {'name': 'Trade Details', 'url': '/api/trades/<transactionId>'},
        {'name': 'Create Cargo Shipment', 'url': '/api/cargo/'},
        {'name': 'Cargo Shipment Details', 'url': '/api/cargo/<shipmentId>'},
        {'name': 'Inventory Details', 'url': '/api/inventory/<stationId>'},
        {'name': 'Real-Time Updates', 'url': '/api/updates/real-time/'},
    ]
    return render(request, 'api_index.html', {'api_urls': api_urls})
