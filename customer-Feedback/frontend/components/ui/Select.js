export default function Select({ options, value, onChange }) {
    return (
      <select
        className="p-2 border rounded-md w-full"
        value={value}
        onChange={onChange}
      >
        {options.map((option, index) => (
          <option key={index} value={option}>
            {option}
          </option>
        ))}
      </select>
    );
  }
  