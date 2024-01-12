import React, { useState, useEffect } from 'react';
import TranslationForm from './TranslationForm';
import TranslationResult from './TranslationResult';
import axios from 'axios';

function App() {
  const [translation, setTranslation] = useState('');
  const [targetLanguage, setTargetLanguage] = useState('es');

  const handleTranslation = async (text) => {
    try {
      const response = await axios.post('http://localhost:8000/translate', {
        text,
        target_language: targetLanguage,
      });
      setTranslation(response.data.translation);
    } catch (error) {
      console.error('Translation error:', error);
    }
  };

  return (
    <div>
      <TranslationForm onTranslation={handleTranslation} />
      <TranslationResult translation={translation} />
    </div>
  );
}

export default App;