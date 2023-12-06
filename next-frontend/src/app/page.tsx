'use client';

import ButtonGroup from "@/components/buttons/ButtonGroup";
import BasicFeed from "@/components/lists/BasicFeed";
import { useState } from "react";

export default function Home() {
  const [locked, setLocked] = useState(false);

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
        <BasicFeed data={[
          {
            timestamp: "2023-12-04",
            caption: "Door Unlocked"
          },
          {
            timestamp: "2023-12-04",
            caption: "Door Locked"
          },
          {
            timestamp: "2023-12-04",
            caption: "Door Unlocked"
          },
        ]}/>
      </div>

    </main>
  )
}
