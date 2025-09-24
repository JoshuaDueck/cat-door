export async function getDoorState() {
  const res = await fetch("http://localhost:5001/api/v1/door", { next: { tags: ["door"], revalidate: 0 } });
  const data = await res.json();
  console.log(data);
  return data;
}

export async function setDoorLock() {
  console.log("setDoorLock");
  const res = await fetch("http://localhost:5001/api/v1/door", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ lock }),
  });
  const data = await res.json();
  return data;
}
