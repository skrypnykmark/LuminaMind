import { Link } from 'react-router-dom'

export default function Disclaimer() {
  return (
    <div className="bg-amber-50/90 border-b border-amber-200/50 px-4 py-3">
      <div className="max-w-4xl mx-auto flex flex-wrap items-center justify-between gap-2 text-sm">
        <p className="text-amber-900">
          Lumina Mind is not medical advice. For emergencies, call{' '}
          <strong>911</strong>. For crisis support, call/text <strong>988</strong>.
        </p>
        <Link
          to="/help"
          className="text-amber-800 font-medium hover:underline whitespace-nowrap"
        >
          Get Help →
        </Link>
      </div>
    </div>
  )
}
