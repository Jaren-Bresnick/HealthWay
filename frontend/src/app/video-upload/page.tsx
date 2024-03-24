'use client'

import { Button, Table } from "@mui/joy"
import IconButton from '@mui/joy/IconButton';
import AddIcon from '@mui/icons-material/Add';
import RemoveIcon from '@mui/icons-material/Remove';
import DeleteIcon from '@mui/icons-material/Delete';
import { useEffect, useState } from "react";
import FormControl from '@mui/joy/FormControl';
import FormLabel from '@mui/joy/FormLabel';
import Input from '@mui/joy/Input';
import Modal from '@mui/joy/Modal';
import ModalDialog from '@mui/joy/ModalDialog';
import DialogTitle from '@mui/joy/DialogTitle';
import DialogContent from '@mui/joy/DialogContent';
import Stack from '@mui/joy/Stack';
import { useRouter } from 'next/navigation'


export default function Home() {

  const router = useRouter()
  const [loading, setLoading] = useState(false);

  const handleVideoUpload = async (event: any) => {
    setLoading(true);
    const file = event.target.files[0];
    if (!file) return;
    const formData = new FormData();
    formData.set('file', file);

    const requestOptions = {
      method: "POST",
      body: formData,
    };

    const data = await fetch("http://127.0.0.1:8000/process_video", requestOptions)

    if (data.status !== 200) {
      alert('Error processing receipt image');
      setLoading(false);
      return;
    }

    setLoading(false);
    router.push('/inventory');
  }


  return (
    <div className='flex flex-row justify-center'>

      <div className='m-10 flex flex-col space-y-4 max-w-[1100px]'>

        <div className='flex flex-col'>
          <p className='font-bold text-2xl'>Video Upload</p>
          <p className='text-slate-500'>Here is a demo of video upload, which shows a request that the in-fridge camera would make to update your inventory whenever there is movement in the fridge.</p>
        </div>

        <div className='flex justify-center'>
          <input type="file" name="video" id="video" className='hidden' accept="image/*" onInput={handleVideoUpload} />
          {!loading ?
            <label
              htmlFor="video"
              className='px-4 py-2 border-2 bg-white w-full rounded-lg text-black text-center hover:cursor-pointer text-sm'>
              Upload Video
            </label> :
            <Button className='bg-white w-full px-4 py-2' loading></Button>
          }
        </div>
      </div>
    </div>
  );
}
