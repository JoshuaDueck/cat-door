import DoorToggle from "@/components/page_elements/DoorToggle";
import LogFeed from "@/components/page_elements/LogFeed";
import { getDoorState } from "@/services/DoorService";

export default async function Home() {
  const initialDoorState = await getDoorState();

  return (
    <main className="">
      <DoorToggle initialDoorState={initialDoorState}/>
      <h2 className="text-xl font-bold mb-2">Recent Activity</h2>
      <LogFeed />
    </main>
  )
}
