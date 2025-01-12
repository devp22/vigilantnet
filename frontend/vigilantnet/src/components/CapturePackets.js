import React, { useState, useEffect } from "react";
import axios from "axios";

const CapturePackets = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await axios("http://localhost:5000/api/packets");
      setData(result.data);
    };

    const interval = setInterval(fetchData, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>Packets Captured</h2>
      {data.length > 0 ? (
        <ul>
          {data.map((packet, index) => (
            <li key={index}>
              <strong>Summary:</strong> {packet.summary} <br />
              <strong>Source:</strong> {packet.src || "N/A"} <br />
              <strong>Destination:</strong> {packet.dst || "N/A"} <br />
              <strong>Type:</strong> {packet.type || "N/A"}
            </li>
          ))}
        </ul>
      ) : (
        <p>No packets captured yet.</p>
      )}
    </div>
  );
};

export default CapturePackets;
