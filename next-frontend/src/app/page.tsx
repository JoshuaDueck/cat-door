import DoorToggle from "@/components/page_elements/DoorToggle";
import LogFeed from "@/components/page_elements/LogFeed";

export default function Home() {
  return (
    <main className="">
      <DoorToggle />
      <h2 className="text-xl font-bold mb-2">Recent Activity</h2>
      <LogFeed />
    </main>
  )
}
