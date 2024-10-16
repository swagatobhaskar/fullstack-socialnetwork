import Image from "next/image";
import bg from '@/public/images/background/bewakoof-unsplash.jpg';
import logo from '@/public/images/logo/social-icons-clipart.png';

export default function Home() {
  return (
    <div>
      <header className="border-b-2 border-blue-50 h-16">
        <Image className="ml-20 my-1 size-14" src={logo} alt="temporary-logo" placeholder="blur"
          quality={80} style={{objectFit: 'cover',}}
        />
      </header>
      <main className="relative h-screen">
        <div className="flex flex-row h-full">
          <aside className="bg-green-600 basis-3/4 relative">
            <div className="absolute inset-0">
              <Image
                alt="two-girls-sitting-on-two-swings-facing-each-other"
                src={bg}
                placeholder="blur"
                quality={100}
                fill
                sizes="70vw"
                style={{objectFit: 'cover',}}
              />
            </div>
          </aside>
          <aside className="basis-1/4 bg-blue-600">
            <div className="">
              <p>Form Section</p>
            </div>
          </aside>
        </div>
      </main>
      <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center">
        <div className="h-16 content-center">
          <p>This is the footer.</p>
        </div>
      </footer>
    </div>
  );
}
