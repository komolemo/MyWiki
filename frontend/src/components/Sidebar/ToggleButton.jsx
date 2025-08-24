import React, { useState } from 'react';
import './ToggleButton.css';

export default function ThemeToggle() {
  const [isDark, setDark] = useState(false);

  const changeTheme = () => {
    setDark(!isDark);
    window.api.toggleChangeTheme();
  }

  return (
    <label className="toggleButton">
      <input
        type="checkbox"
        className="toggleButton__checkbox"
        checked={isDark}
        onChange={changeTheme}
      />
    </label>
  );
}