export default function Input({ type, onChange }) {
    return (
      <input
        type={type}
        className="p-2 border rounded-md w-full"
        onChange={onChange}
      />
    );
  }
  