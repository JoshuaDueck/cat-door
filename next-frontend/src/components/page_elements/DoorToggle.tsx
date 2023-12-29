'use client';

import { useEffect, useState } from "react";
import ButtonGroup from "../buttons/ButtonGroup"
import { getDoorState } from "@/services/DoorService";

export default function DoorToggle({}:{}) {
  const [locked, setLocked] = useState(false);

  useEffect(() => {
    const fetchDoorState = async () => {
      const doorState = await getDoorState();
      setLocked(doorState['data']['locked']);
    }
  });

  return (
    <>
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
    </>
  )
}
