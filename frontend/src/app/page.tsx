import RecipeCard from "./components/recipe-card";

export default function Home() {
  return (
    <div className='flex flex-row justify-center'>

      <div className='m-10 flex flex-col space-y-4 max-w-[1100px] w-full'>

        <div className='flex flex-col text-start'>
          <p className='font-bold text-2xl'>Good Afternoon, Shrisha</p>
          <p className='text-slate-500'>Today is Sunday. Welcome to HealthView. Use the dashboard below to see your personalized recipies, what pills you need to take, and the inventory of food that you have.</p>
        </div>

        <div className='grid grid-cols-1 lg:grid-cols-2 gap-2'>

          <a href="/inventory">
            <div className='border rounded-lg shadow-sm p-4 flex flex-col space-y-2'>
              <p className='text-xl font-semibold'>Inventory</p>
              <img src='inventory.png' className='object-scale-down h-52' />
            </div>
          </a>


          <div className='border rounded-lg shadow-sm p-4 row-span-2 flex flex-col space-y-2'>
            <a href="/recipes">
              <p className='text-xl font-semibold'>Recipes</p>
              <img src='recipes.png' className='rounded-lg' />
            </a>
          </div>


          <a href='/pills'>
            <div className='border rounded-lg shadow-sm p-4 flex flex-col space-y-2'>
              <p className='text-xl font-semibold'>Pills</p>
              <img src='pills.png' className='object-scale-down h-52' />
            </div>

          </a>


        </div>


      </div>



    </div>
  );
}
