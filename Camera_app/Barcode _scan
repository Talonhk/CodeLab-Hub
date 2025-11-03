import React, { useState, useRef } from "react";

// Dummy barcode scanner function (replace with real scanner logic/library)
function mockScanBarcode() {
  // Simulate a scan result with a random barcode
  const barcodes = [
    { code: "123456789012", name: "Milk" },
    { code: "987654321098", name: "Bread" },
    { code: "555555555555", name: "Eggs" }
  ];
  return barcodes[Math.floor(Math.random() * barcodes.length)];
}

function BarcodeScanner() {
  const videoRef = useRef(null);
  const [items, setItems] = useState([]);
  const [taxRate, setTaxRate] = useState(0.07); // 7% default tax

  // Simulate scanning and adding an item
  const handleScan = () => {
    const scanned = mockScanBarcode();
    setItems([
      ...items,
      { code: scanned.code, name: scanned.name, price: 0.00 }
    ]);
  };

  // Update price for an item
  const handlePriceChange = (idx, value) => {
    const updated = [...items];
    updated[idx].price = parseFloat(value) || 0;
    setItems(updated);
  };

  // Calculate subtotal and tax
  const subtotal = items.reduce((sum, item) => sum + item.price, 0);
  const tax = subtotal * taxRate;
  const total = subtotal + tax;

  return (
    <div>
      <h2>Barcode Scanner</h2>
      <video ref={videoRef} autoPlay style={{ width: "100%", maxWidth: 400 }} />
      <button onClick={handleScan}>Scan Barcode (Demo)</button>
      <ul>
        {items.map((item, idx) => (
          <li key={item.code + idx}>
            {item.name} ({item.code}) - 
            <input
              type="number"
              step="0.01"
              value={item.price}
              onChange={e => handlePriceChange(idx, e.target.value)}
              style={{ width: "80px", marginLeft: "8px" }}
            /> $
          </li>
        ))}
      </ul>
      <div style={{ marginTop: "16px" }}>
        <label>
          Local Tax Rate:
          <input
            type="number"
            step="0.01"
            value={taxRate}
            onChange={e => setTaxRate(parseFloat(e.target.value) || 0)}
            style={{ width: "60px", marginLeft: "8px" }}
          />
        </label>
      </div>
      <div style={{ marginTop: "16px" }}>
        <strong>Subtotal:</strong> ${subtotal.toFixed(2)} <br />
        <strong>Tax:</strong> ${tax.toFixed(2)} <br />
        <strong>Total:</strong> ${total.toFixed(2)}
      </div>
      {/* Barcode result will be displayed here */}
      <p>Scan a barcode using your phone's camera.</p>
    </div>
  );
}

export default BarcodeScanner;