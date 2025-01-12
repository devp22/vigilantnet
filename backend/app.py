from scapy.all import sniff
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

def packet_handler(packet):
    return {
        "summary": packet.summary(),  
        "src": packet.src if hasattr(packet, "src") else None,
        "dst": packet.dst if hasattr(packet, "dst") else None,
        "type": packet.type if hasattr(packet, "type") else None,
    }

@app.route('/api/packets', methods=['GET'])
def get_packets():
    # Sniff 10 packets and process them with packet_handler
    packets = sniff(count=10)
    processed_packets = [packet_handler(packet) for packet in packets]
    return jsonify(processed_packets)  

if __name__ == '__main__':
    app.run(debug=True)
