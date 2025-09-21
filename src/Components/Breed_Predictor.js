// src/components/BreedPredictor.js
import React, { useState } from 'react';
import './Breed_Predictor.css';

function BreedPredictor() {
  const [image, setImage] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [result, setResult] = useState('');
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);
  const [summaryLoading] = useState(false);


  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setImage(file);
    setPreviewUrl(URL.createObjectURL(file));
    setResult('');
    setSummary('');
  };

  const handlePredict = async () => {
    if (!image) {
      alert('Please upload an image.');
      return;
    }

    setLoading(true);
    setSummary('');
    const formData = new FormData();
    formData.append('image', image);

    try {
      const res = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        body: formData
      });

      const data = await res.json();

      if (data.error) {
        setResult('Error: ' + data.error);
        setSummary('');
        return;
      }

      const output =
        `Animal: ${data.animal}\n` +
        `Breed: ${data.breed}\n` +
        `Breed Confidence: ${(data.confidence * 100).toFixed(2)}%\n` +
        `Animal Confidence: ${(data.animal_confidence * 100).toFixed(2)}%`;

      setResult(output);

      // Use summary from /predict API response directly
      setSummary(data.summary || 'No summary available.');

    } catch (error) {
      setResult('Error: ' + error.message);
      setSummary('');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="predictor-container">
      <h2>Cow/Buffalo Breed Predictor</h2>
      <input type="file" accept="image/*" onChange={handleImageChange} />
      <button onClick={handlePredict} disabled={loading}>
        {loading ? 'Predicting...' : 'Predict'}
      </button>
      {previewUrl && <img src={previewUrl} alt="Preview" className="preview" />}
      <pre className="result">{result}</pre>
      {result && (
        // Inside your BreedPredictor.js component, in the JSX where you display summary:

          <div className="breed-info">
            <h3>Breed Information</h3>
            {summaryLoading ? (
              <p>Loading breed information...</p>
            ) : (
              <ul className="summary-list">
                {summary
                  .split('*')
                  .map(item => item.trim())
                  .filter(item => item.length > 0)
                  .map((point, idx) => (
                    <li key={idx}>{point}</li>
                  ))
                }
              </ul>
            )}
          </div>

      )}
    </div>
  );
}

export default BreedPredictor;
