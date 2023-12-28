'use client';

import ButtonGroup from "@/components/buttons/ButtonGroup";
import BasicFeed from "@/components/lists/BasicFeed";
import { getRecentLogEntries } from "@/services/LogService";
import { useState } from "react";

export default async function Home() {
  const [locked, setLocked] = useState(false);

  // const log_data = fetch('/api/v1/log_entries')
  // const feed_data = log_data.map((entry) => {
  //   return {
  //   caption: entry.action,
  //     timestamp: entry.timestamp
  //   }
  // }

  return (
    <main className="">
      <h2 className="text-xl font-bold">Door Status: {locked ? 'Locked' : 'Unlocked'}</h2>
      <ButtonGroup
        className="mb-4"
        buttons={[
          {
            label: "Locked",
            active: locked,
            onClick: () => {setLocked(true)}
          },
          {
            label: "Unlocked",
            active: !locked,
            onClick: () => {setLocked(false)}
          }
        ]}
      />
      <h2 className="text-xl font-bold">Recent Activity</h2>

      <div className="flex flex-row justify-between">
        <BasicFeed data={feed_data}/>
      </div>

    </main>
  )
}
