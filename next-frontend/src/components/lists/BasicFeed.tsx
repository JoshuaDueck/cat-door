import React from "react";

export default function BasicFeed({
  data
}: {
  data: {
    timestamp: string
    caption: React.ReactNode
  }[]
}) {
  return (
  <div className="flow-root">
    <ul role="list" className="-mb-8">
      {
        data.map((item, index) => (
          <li className="group" key={index}>
            <div className="relative pb-8">
              <span className="absolute left-4 top-4 -ml-px h-full w-0.5 bg-gray-200 group-last:hidden" aria-hidden="true"></span>
              <div className="relative flex space-x-3">
                <div>
                  <span className="h-8 w-8 rounded-full bg-gray-400 flex items-center justify-center ring-8 ring-white">
                    <svg className="h-5 w-5 text-white" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                      <path d="M10 8a3 3 0 100-6 3 3 0 000 6zM3.465 14.493a1.23 1.23 0 00.41 1.412A9.957 9.957 0 0010 18c2.31 0 4.438-.784 6.131-2.1.43-.333.604-.903.408-1.41a7.002 7.002 0 00-13.074.003z" />
                    </svg>
                  </span>
                </div>
                <div className="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
                  <div>
                    <p className="text-sm text-gray-800 font-bold">{item.caption}</p>
                  </div>
                  <div className="whitespace-nowrap text-right text-sm text-gray-500">
                    <time dateTime={item.timestamp}>{item.timestamp}</time>
                  </div>
                </div>
              </div>
            </div>
          </li>
        ))
      }
    </ul>
  </div>

  );
}
