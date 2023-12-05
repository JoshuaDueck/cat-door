'use client';

export default function ButtonGroup({
    buttons,
    ...props
}: {
    buttons: {
        label: string
        active?: boolean
        activeColor?: string
        onClick: () => void
    }[],
    className?: string
}) {
    return (
        <span className={`isolate inline-flex rounded-md shadow-sm ${props.className}`}>
            {buttons.map((button, index) => (
                <button
                    key={index}
                    type="button"
                    className={`relative -ml-px first:ml-0 inline-flex first:rounded-l-md last:rounded-r-md items-center px-3 py-2 text-sm font-semibold ring-1 ring-inset focus:z-10
                        ${button.active ? `bg-${button.activeColor || 'indigo'}-600 hover:bg-${button.activeColor || 'indigo'}-600 hover:cursor-default text-white ring-${button.activeColor || 'indigo'}-700` : 'bg-white hover:bg-gray-50 text-gray-900 ring-gray-300'}`}
                    onClick={button.onClick}
                >
                    {button.label}
                </button>
            ))}
        </span>
    )
}
