import React, { useState, useEffect } from 'react';

function TranslationForm({ onTranslation }) {
  const [text, setText] = useState('');

  useEffect(() => {
    const timer = setTimeout(() => {
      if (text.trim() !== '') {
        onTranslation(text);
      }
    }, 1000);

    return () => clearTimeout(timer);
  }, [text, onTranslation]);

  return (
    <div>
      <textarea value={text} onChange={(e) => setText(e.target.value)} />
    </div>
  );
}

export default TranslationForm;