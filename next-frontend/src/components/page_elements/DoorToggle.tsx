'use client';

import { useQuery } from "@tanstack/react-query";
import ButtonGroup from "../buttons/ButtonGroup"
import { setDoorLock } from "@/services/DoorService";

export default function DoorToggle() {
  const lockDoor = useQuery({ queryKey: ['door'], queryFn: setDoorLock })

  return (
    <>
      <h2 className="text-xl font-bold">Door Status: {locked ? 'Locked' : 'Unlocked'}</h2>
      <ButtonGroup
        className="mb-4"
        buttons={[
          {
            label: "Locked",
            active: locked,
            onClick: () => {}
          },
          {
            label: "Unlocked",
            active: !locked,
            onClick: () => {}
          }
        ]}
      />
    </>
  )
}
